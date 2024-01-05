using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementPath : MonoBehaviour
{
    public int movementDirection = 1;
    public int movingTo = 0;
    public Transform[] PathElements;

    public void OnDrawGizmos()
    {
        if (PathElements == null || PathElements.Length < 2)
        {
            return;
        }

        for (var i = 1; i < PathElements.Length; i++)
        {
            Gizmos.DrawLine(PathElements[i - 1].position, PathElements[i].position);
        }

        Gizmos.DrawLine(PathElements[0].position, PathElements[PathElements.Length-1].position);

    }

    public IEnumerator<Transform> GetNextPathPoint()
    {
        if(PathElements == null ||PathElements.Length < 1)
        {
            yield break;
        }

        while (true)
        {
            yield return PathElements[movingTo];

            if(PathElements.Length == 1)
            {
                continue;
            }

        
            movingTo = movingTo + movementDirection;

            if (movingTo >= PathElements.Length)
            {
                movingTo = 0;
            }

            if (movingTo < 0)
            {
                movingTo = PathElements.Length - 1;
            }
          
        }
    }
   

}

