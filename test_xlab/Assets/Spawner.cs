using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject myObj;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.X))
        {
            Instantiate(myObj, transform.position, Quaternion.identity);
        }
        
    }
}
