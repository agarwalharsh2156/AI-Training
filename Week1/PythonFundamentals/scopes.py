### Understanding nonlocal statements.###
# Below given count variable belong to local scope of outer_func()
def outer_func():
    count = 0
    def inner_func():
        # by using nonlocal statement, we can tell python that this variable lies outside the current function's scope
        # which makes python look for the variable over there and will not create a new variable for the namespace of inner_func()
        nonlocal count
        count = 1
        print("inner function count is: ", count)
        print(id(count))
    inner_func()
    print("outer function count is: ", count)
    print(id(count))


# both count variables lie on different address because they have innermost scope if you don't use nonlocal statement inside the inner_func
# once you use nonlocal in inner_func() it will make python to look for the variable outside the scope of inner_func namespace.
outer_func()

###################################################################################################################################################


### Understanding global statement
# Below given app_state variable belongs to a global scope (module level).
app_state = "running"

def run_app():
    # Without using global statement python will create a new app_state variable for run_app namespace.
    # to prevent this and tell python that this is a global variable we use global statement.
    global app_state
    app_state = "stopped"
    print("App Status inside run_app: ", app_state)
    print(id(app_state))

run_app()

# while you don't use global statement for app_state inside app_run function
# you see that both ids for app_state are different inside and outside the funciton.
print("App Status outside run_app: ", app_state)
print(id(app_state))
