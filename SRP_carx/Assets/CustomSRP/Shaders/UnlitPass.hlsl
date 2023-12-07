﻿#ifndef CUSTOM_UNLIT_PASS_INCLUDED
#define CUSTOM_UNLIT_PASS_INCLUDED

#include "../ShaderLibrary/Common.hlsl"

TEXTURE2D(_BaseMap);
SAMPLER(sampler_BaseMap);

CBUFFER_START(UnityPerMaterial)
	float4 _BaseColor;
	float4 _BaseMap_ST; //texture scale and transform params
	float _Cutoff;
CBUFFER_END

struct VertexAttributes {
	float3 positionOS : POSITION;
	float2 uv         : TEXCOORD0;
};

struct Varyings {
	float4 positionCS : SV_POSITION;
	float2 uv         : TEXCOORD0;
};

Varyings Vertex(VertexAttributes vertexInput)
{
	Varyings vertexOut;
	float3 positionWS = TransformObjectToWorld(vertexInput.positionOS.xyz);
	vertexOut.positionCS = TransformWorldToHClip(positionWS);
	vertexOut.uv = vertexInput.uv * _BaseMap_ST.xy + _BaseMap_ST.zw;

	return vertexOut;
}

float4 Fragment(Varyings fragmentInput) : SV_TARGET
{
	float4 baseMapColor = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, fragmentInput.uv);
	float4 base = baseMapColor * _BaseColor;
	clip(base.a - _Cutoff);
	return base;
}

#endif