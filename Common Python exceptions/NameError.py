def myfunction():
    local_var = 10

    print(local_var, sqrt(local_var))  # * NameError: name 'local_var' is not defined


myfunction()
