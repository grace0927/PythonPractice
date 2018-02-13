import beyond_the_basics.registry as registry

registry.registry('name')
for name in registry.registry_names():
    print(name)
