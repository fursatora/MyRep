Shader "CustomSRP/Lit"
{
	Properties
	{
		_BaseMap("Texture", 2D) = "white" {}
		_BaseColor("Color", Color) = (1.0, 1.0, 1.0, 1.0)
		_Metalness ("Metalness", Range(0, 1)) = 0
		_Roughness ("Roughness", Range(0, 1)) = 0.5
		[Enum(UnityEngine.Rendering.BlendMode)] _SrcBlend ("Src Blend", Float) = 1
		[Enum(UnityEngine.Rendering.BlendMode)] _DstBlend ("Dst Blend", Float) = 0
		[Enum(Off, 0, On, 1)] _ZWrite ("Z Write", Float) = 1
		[Enum(Off, 0, On, 1)] _CastShadows("Cast Shadows", Float) = 1
		[Enum(Off, 0, On, 1)] _ReceiveShadows("Receive Shadows", Float) = 1
	}

	SubShader
	{
		Pass
		{
			Tags {
				"LightMode" = "CustomLit"
			}

			Blend [_SrcBlend] [_DstBlend]
			ZWrite [_ZWrite]

			HLSLPROGRAM
			#pragma target 3.5
			#pragma vertex Vertex
			#pragma fragment Fragment
			#include "LitPass.hlsl"
			ENDHLSL

		}
		


	}
}