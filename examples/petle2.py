promienie_odwarznikuw = {"2kg": 5, "10kg": 10, "1kg": 6,"20kg": 20}
for masa in promienie_odwarznikuw:
    promien = promienie_odwarznikuw[masa]
    powierzchnia = promien * promien * 3.14
    print "powierzchnia odwaznika o masie %s i promieniu %s cm = %s cm2" % (masa, promien, powierzchnia)
