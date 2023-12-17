﻿#ifndef CUSTOM_LIT_PASS_INCLUDED
#define CUSTOM_LIT_PASS_INCLUDED

#include "../ShaderLibrary/Common.hlsl"
#include "../ShaderLibrary/Surface.hlsl"
#include "../ShaderLibrary/Light.hlsl"
#include "../ShaderLibrary/BRDF.hlsl"
#include "../ShaderLibrary/Lighting.hlsl"


TEXTURE2D(_BaseMap);
SAMPLER(sampler_BaseMap);

CBUFFER_START(UnityPerMaterial)
	float4 _BaseColor;
	float4 _BaseMap_ST; //texture scale and transform params
	float _Metalness;
	float _Roughness;
CBUFFER_END

struct VertexAttributes {
	float3 positionOS : POSITION;
	float3 normalOS   : NORMAL;
	float2 uv         : TEXCOORD0;
};

struct Varyings {
	float4 positionCS : SV_POSITION;
	float3 positionWS : VAR_POSITION;
	float3 normalWS   : VAR_NORMAL;
	float2 uv         : TEXCOORD0;
};

Varyings Vertex(VertexAttributes vertexInput)
{
	Varyings vertexOut;
	vertexOut.positionWS = TransformObjectToWorld(vertexInput.positionOS.xyz);
	vertexOut.positionCS = TransformWorldToHClip(vertexOut.positionWS);
	vertexOut.normalWS = TransformObjectToWorldNormal(vertexInput.normalOS);
	vertexOut.uv = vertexInput.uv * _BaseMap_ST.xy + _BaseMap_ST.zw;

	return vertexOut;
}


float4 Fragment(Varyings fragmentInput) : SV_TARGET
{
	float4 baseColor = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, fragmentInput.uv);
	baseColor *= _BaseColor;

	Surface surface;
	surface.normal = normalize(fragmentInput.normalWS);
	surface.viewDirection = normalize(_WorldSpaceCameraPos - fragmentInput.positionWS);
	surface.color = baseColor.rgb;
	surface.alpha = baseColor.a;
	surface.metalness = _Metalness;
	surface.roughness = _Roughness;

	BRDF brdf = GetBRDF(surface);
	float3 color = GetLighting(surface, brdf);


	return float4(color, surface.alpha);
}



#endif