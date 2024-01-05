using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeItem : MonoBehaviour
{
    public GameObject first;
    public GameObject second;
    private bool used = false;

    void Start()
    {
        second.SetActive(false);
    }

    
    void Update()
    {
        if (!used && Input.GetKeyDown(KeyCode.Space))
        {
            Replace(first, second);
            Debug.Log("Replaced");
            used = true;
        }
    }

    void Replace(GameObject first, GameObject second)
    {
        //Instantiate(second, first.transform.position, Quaternion.identity);
        second.SetActive(true);
        Destroy(first);
    }
}
