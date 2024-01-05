using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FollowPath : MonoBehaviour
{
    public MovementPath MyPath;
    public float speed = 1;
   

    private IEnumerator<Transform> pointInPath;

    void Start()
    {
        if (MyPath == null)
        {
            Debug.Log("Примени путь");
            return;
        }

        pointInPath = MyPath.GetNextPathPoint();

        pointInPath.MoveNext();

        if (pointInPath.Current == null)
        {
            Debug.Log("Нужны точки");
            return;
        }
        transform.position = pointInPath.Current.position;
    }

    void Update()
    {
        if (pointInPath == null || pointInPath.Current == null)
        {
            return;
        }

        transform.position = Vector3.Lerp(transform.position, pointInPath.Current.position, Time.deltaTime * speed);
        

        if (Input.GetKeyDown(KeyCode.Z))
        {
            pointInPath.MoveNext();
        }
    }
}
