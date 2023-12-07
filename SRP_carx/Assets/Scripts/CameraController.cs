using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public Camera cam;
    public Transform target;
    public float speedX = 360f;
    public float speedY = 240f;
    public float limitY = 40f;
    public float minDistancet = 1.5f;
    public LayerMask obstacles;
    private float _maxDistance;
    private Vector3 _localPosition;
    private float _currentYRotation;
    private LayerMask _camOrigin;

    private Vector3 _position
    {
        get { return transform.position; }
        set { transform.position = value; }
    }

    void Start()
    {
        _localPosition = target.TransformPoint(_position);
        _maxDistance = Vector3.Distance(_position, target.position);

    }

    void LateUpdate()
    {
        _position = target.TransformPoint(_localPosition);
        CameraRotation();
        ObstaclesReact();

        _localPosition = target.InverseTransformPoint(_position);

    }
    void CameraRotation()
    {
        var mx = -Input.GetAxis("Mouse X");
        var my = -Input.GetAxis("Mouse Y");

        if (my != 0)
        {
            var tmp = Mathf.Clamp(_currentYRotation + my * speedY * Time.deltaTime, -limitY, limitY);
            if (tmp != _currentYRotation)
            {
                var rot = tmp - _currentYRotation;
                transform.RotateAround(target.position, transform.right, rot);
                _currentYRotation = tmp;
            }
        }
        if( mx != 0)
        {
            transform.RotateAround(target.position, Vector3.up, mx * speedX * Time.deltaTime);
        }
        transform.LookAt(target);

    }

    void ObstaclesReact()
    {
        var distance = Vector3.Distance(_position, target.position);
        RaycastHit hit;
        if (Physics.Raycast(target.position, transform.position - target.position, out hit, _maxDistance, obstacles))
        {
            _position = hit.point;
        }
        else if (distance < _maxDistance && !Physics.Raycast(_position, -transform.forward, .1f, obstacles))
        {
            _position -= transform.forward * .05f;
        }
    }

}
