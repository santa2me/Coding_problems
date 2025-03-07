def asteroidCollision(asteroids):
    stack = []
    count = 0

    for i, a in enumerate(asteroids):
        if stack and stack[-1] > 0 and a < 0:
            while count > 0:
                right = stack[-1]
                if abs(right) < abs(a):
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(a)
                        break
                    else:
                        count -= 1
                elif abs(right) == abs(a):
                    stack.pop()
                    break
                else:
                    break
        else:
            if a > 0:
                count += 1
            stack.append(a)

    return stack
asteroidCollision([1,-2,-2,-2])
        