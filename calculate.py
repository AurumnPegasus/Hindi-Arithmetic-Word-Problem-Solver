def eq_builder(karta, karma, verb_type, value, sampradaan, c_values):
    if verb_type == 't-':
        values = []
        values_s = []
        is_karta_present = False
        is_karma_present_1 = False
        is_karma_present_2 = False
        is_sampradaan_present = False
        location_karta = 0
        location_karma_1 = 0
        location_karma_2 = 0
        location_sampradaan = 0

        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            if c_value[0] == sampradaan:
                is_sampradaan_present = True
                values_s.append(int(location_sampradaan))
            location_karta += 1
            location_sampradaan += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present_1 = True
                    break
                location_karma_1 += 1
        if is_sampradaan_present:
            for location in values_s:
                if c_values[location][2] == karma:
                    is_karma_present_2 = True
                    break
                location_karma_2 += 1

        if is_karta_present and is_karma_present_1 and is_karma_present_2 and is_sampradaan_present:
            present_1 = float(c_values[values[location_karma_1]][1])
            present_2 = float(c_values[values_s[location_karma_2]][1])
            c_values[values[location_karma_1]] = [karta, present_1 + float(value), karma]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 - float(value), karma]
        elif is_karta_present and is_karma_present_1:
            present_1 = float(c_values[values[location_karma_1]][1])
            c_values[values[location_karma_1]] = [karta, present_1 + float(value), karma]
            c_values.append([sampradaan, -1*float(value), karma])
        elif is_karma_present_2 and is_sampradaan_present:
            present_2 = float(c_values[values_s[location_karma_2]][1])
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 - float(value), karma]
            c_values.append([karta, float(value), karma])
        else:
            c_values.append([karta, float(value), karma])
            c_values.append([sampradaan, -1*float(value), karma])

    if verb_type == 't+':
        values = []
        values_s = []
        is_karta_present = False
        is_karma_present_1 = False
        is_karma_present_2 = False
        is_sampradaan_present = False
        location_karta = 0
        location_karma_1 = 0
        location_karma_2 = 0
        location_sampradaan = 0

        for c_value in c_values:
            if c_value[0] == karta:
                is_karta_present = True
                values.append(int(location_karta))
            if c_value[0] == sampradaan:
                is_sampradaan_present = True
                values_s.append(int(location_sampradaan))
            location_karta += 1
            location_sampradaan += 1

        if is_karta_present:
            for location in values:
                if c_values[location][2] == karma:
                    is_karma_present_1 = True
                    break
                location_karma_1 += 1
        if is_sampradaan_present:
            for location in values_s:
                if c_values[location][2] == karma:
                    is_karma_present_2 = True
                    break
                location_karma_2 += 1

        if is_karta_present and is_karma_present_1 and is_karma_present_2 and is_sampradaan_present:
            present_1 = float(c_values[values[location_karma_1]][1])
            present_2 = float(c_values[values_s[location_karma_2]][1])
            c_values[values[location_karma_1]] = [karta, present_1 - float(value), karma]
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 + float(value), karma]
        elif is_karta_present and is_karma_present_1:
            present_1 = float(c_values[values[location_karma_1]][1])
            c_values[values[location_karma_1]] = [karta, present_1 - float(value), karma]
            c_values.append([sampradaan, float(value), karma])
        elif is_karma_present_2 and is_sampradaan_present:
            present_2 = float(c_values[values_s[location_karma_2]][1])
            c_values[values_s[location_karma_2]] = [sampradaan, present_2 + float(value), karma]
            c_values.append([karta, -1*float(value), karma])
        else:
            c_values.append([karta, -1*float(value), karma])
            c_values.append([sampradaan, float(value), karma])
        
    return c_values