service = [("web-app", 3), ("database", 2), ("cache", 5), ("api-gateway", 2)]

print(f"Default Sort: {sorted(service)}")


def sorting_func(svc):
    return svc[1]


print(f"Sorting by replica count - standard function: {sorted(service, key=sorting_func)}")