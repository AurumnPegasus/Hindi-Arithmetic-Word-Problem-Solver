c_values = []

def eq_build(karta, verb_type, value, karma, karta_number, recepient):
    counter = 0
    if karta_number == 1 :                                          # container [ ram ]
        if verb_type == '0' :                               
            if counter == 0:
                c_values.append([int(value), karma])                # value, object         c_values = [ [4, neeli ball ] ]
                counter += 1                                        # decleration is over
            else:
                ispresent = False           
                location = len(c_values) -1                         # location is 0
                for c_value in c_values:        
                    if karma in c_value[1]:                         # karma is object, therefore m searching for if predeclared object is present in the sentence
                        ispresent = True                            # object is repeated
                        location -= 1                               # location is -1
                        break
                if ispresent == True:
                    c_values[location][0] = int(value)              # so...m assigning particular new value to that object
                else:
                    c_values.append([int(value), karma])            # m creating another entry into c_values  c_values = [ [4, neeli ball], [6, hari ball] ]
        if verb_type == 't+' :
            if counter == 0:
                c_values.append([int(value), karma])
                c_values.append([-1*int(value), recepient])
                counter += 1
            else:
                ispresent_1 = False
                ispresent_2 = False
                location_1 = len(c_values) -1
                location_2 = len(c_values) -1
                for c_value in c_values:
                    if karma in c_value[1]:
                        ispresent_1 = True
                        location_1 -= 1
                        break
                for c_value in c_values:
                    if recepient in c_value[1]:
                        ispresent_2 = True
                        location_2 -= 1
                        break
                if ispresent_1 == True and ispresent_2 == True:
                    v1 = c_values[location_1][0]
                    v2 = c_values[location_2][0]
                    c_values[location_1][0] = v1 + int(value)
                    c_values[location_2][0] = v2 - int(value)
                elif ispresent_1 == True and ispresent_2 == False:
                    v1 = c_values[location_1][0]
                    c_values[location_1][0] = v1 + int(value)
                    c_values.append([-1*int(value), recepient])
                elif ispresent_1 == False and ispresent_2 == True:
                    v2 = c_values[location_2][0]
                    c_values[location_2][0] = v2 - int(value)
                    c_values.append([int(value), recepient])
                elif ispresent_1 == False and ispresent_2 == False:    
                    c_values.append([int(value), karma])
                    c_values.append([-1*int(value), recepient])
        if verb_type == 't-' :                                      # verb is di, container = [ Ram, Harry ] 
            if counter == 0:
                c_values.append([-1*int(value), karma])             # c_values = [ [4, neeli ball], [6, hari ball], [-3, neeli ball]]
                c_values.append([int(value), recepient])            # c_values = [ [4, neeli ball], [6, hari ball], [-3, neeli ball], [3, Harry]]
                counter += 1
            else:
                ispresent_1 = False
                ispresent_2 = False
                location_1 = len(c_values) -1
                location_2 = len(c_values) -1                       # both are equal to 3
                for c_value in c_values:
                    if karma in c_value[1]:                         # going through all objects where karma = neeli ball
                        ispresent_1 = True
                        location_1 -= 1                             
                        break
                for c_value in c_values:
                    if recepient in c_value[1]:                     # if Harry is present, which is
                        ispresent_2 = True
                        location_2 -= 1
                        break
                if ispresent_1 == True and ispresent_2 == True:
                    v1 = c_values[location_1][0]    
                    v2 = c_values[location_2][0]
                    c_values[location_1][0] = v1 - int(value)       # should not be negative, since I have already stored negative of that value
                    c_values[location_2][0] = v2 + int(value)       # need not be added, since I have already declared Harry to be 3
                elif ispresent_1 == True and ispresent_2 == False:
                    v1 = c_values[location_1][0]
                    c_values[location_1][0] = v1 - int(value)
                    c_values.append([-1*int(value), recepient])
                elif ispresent_1 == False and ispresent_2 == True:
                    v2 = c_values[location_2][0]
                    c_values[location_2][0] = v2 + int(value)
                    c_values.append([int(value), recepient])
                elif ispresent_1 == False and ispresent_2 == False:    
                    c_values.append([-1*int(value), karma])
                    c_values.append([int(value), recepient])
        if verb_type == '++' :
            if counter == 0:
                c_values.append([int(value), karma])
                counter += 1
            else:
                ispresent = False
                location = len(c_values) -1
                for c_value in c_values:
                    if karma in c_value[1]:
                        ispresent = True
                        location -= 1
                        break
                if ispresent == True:
                    existing_value = c_values[location][0]
                    c_values[location][0] = existing_value + int(value)
                else:
                    c_values.append([int(value), karma])
        if verb_type == '-' :
            if counter == 0:
                c_values.append([int(value), karma])
                counter += 1
            else:
                ispresent = False
                location = len(c_values) -1
                for c_value in c_values:
                    if karma in c_value[1]:
                        ispresent = True
                        location -= 1
                        break
                if ispresent == True:
                    existing_value = c_values[location][0]
                    c_values[location][0] = existing_value - int(value)
                else:
                    c_values.append(-1*[int(value), karma])
        if verb_type == '--' :
            if counter == 0:
                c_values.append([int(value), karma])
                counter += 1
            else:
                ispresent = False
                location = len(c_values) -1
                for c_value in c_values:
                    if karma in c_value[1]:
                        ispresent = True
                        location -= 1
                        break
                if ispresent == True:
                    existing_value = c_values[location][0]
                    c_values[location][0] = existing_value - int(value)
                else:
                    c_values.append(-1*[int(value), karma])