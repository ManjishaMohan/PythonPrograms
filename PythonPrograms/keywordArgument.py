def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print “ % s == % s” % (key, value)

greet_me(name="yasoob”)
name== "yasoob"

#https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/

def test_var_args(f_arg, *argv):
    print “first normal arg:”, f_arg
    for arg in argv:
        print( “another arg through *argv :”, arg)

test_var_args('yasoob’,’python’,’eggs’,’test’)

