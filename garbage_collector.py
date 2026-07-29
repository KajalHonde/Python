import gc

print("Garbage collector is enabled",gc.isenabled())

gc.enable()
print("Garbage collector is enabled",gc.isenabled())

gc.disable()
print("garbage collector is disable",gc.isenabled())