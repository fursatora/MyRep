using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ParticleControl : MonoBehaviour
{
    public ParticleSystem rain;
    public Rigidbody cloud;
  

    void Start()
    {
        rain.Stop();
    }

    void Update()
    {

        rain.Stop();

        if (cloud.velocity.y != 0.0f || cloud.velocity.x != 0.0f || cloud.velocity.z != 0.0f)
        {
            rain.Stop();
        }
        else
        {
            rain.Play();
        }
    }

}
