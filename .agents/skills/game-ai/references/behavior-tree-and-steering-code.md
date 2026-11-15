# Behavior Tree & Steering Behaviors Implementation

## Minimal Behavior Tree Core (C#)
```csharp
public enum NodeState { Running, Success, Failure }

public abstract class BTNode {
    public abstract NodeState Tick();
}

public class Selector : BTNode {
    protected List<BTNode> children;
    public Selector(List<BTNode> nodes) => children = nodes;

    public override NodeState Tick() {
        foreach (var node in children) {
            var state = node.Tick();
            if (state != NodeState.Failure) return state; // Return on Running or Success
        }
        return NodeState.Failure;
    }
}

public class Sequence : BTNode {
    protected List<BTNode> children;
    private int current = 0;
    public Sequence(List<BTNode> nodes) => children = nodes;

    public override NodeState Tick() {
        while (current < children.Count) {
            var state = children[current].Tick();
            if (state == NodeState.Running) return NodeState.Running;
            if (state == NodeState.Failure) {
                current = 0;
                return NodeState.Failure;
            }
            current++;
        }
        current = 0;
        return NodeState.Success;
    }
}
```

## Reynolds Steering Forces
```csharp
public class SteeringPhysics {
    public static Vector3 Seek(Vector3 currentPos, Vector3 currentVel, Vector3 targetPos, float maxSpeed) {
        Vector3 desired = (targetPos - currentPos).normalized * maxSpeed;
        return desired - currentVel;
    }

    public static Vector3 Flee(Vector3 currentPos, Vector3 currentVel, Vector3 threatPos, float maxSpeed) {
        Vector3 desired = (currentPos - threatPos).normalized * maxSpeed;
        return desired - currentVel;
    }

    public static Vector3 Arrive(Vector3 currentPos, Vector3 currentVel, Vector3 targetPos, float maxSpeed, float slowingRadius) {
        Vector3 toTarget = targetPos - currentPos;
        float distance = toTarget.magnitude;
        if (distance < 0.001f) return -currentVel;
        float rampedSpeed = maxSpeed * (distance / slowingRadius);
        float clippedSpeed = Mathf.Min(rampedSpeed, maxSpeed);
        Vector3 desired = (clippedSpeed / distance) * toTarget;
        return desired - currentVel;
    }
}
```
