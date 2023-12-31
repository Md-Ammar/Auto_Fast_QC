def checker(prim_list, sec_list):
    prim_list = prim_list.strip(";").split(";")
    sec_list = sec_list.strip(";").split(';')

    missing = 0

    for item in prim_list:
        if item not in sec_list:
            missing += 1
            print(f"missing value {item}")

    print("missing", missing)

prim_list = 'Alternative Class - Online Processing Systems with Omkar Deshpande;'\
            'Alternative Class - Online Processing Systems Slides by Omkar Deshpande;'\
            'Alternative Class - Online Processing Systems Slides by Sanjay Aggarwal;'\
            'Alternative Class 2 - Online Processing Systems Slides by Niloy Mukherjee;'\
            'Alternative Class 1 - Online Processing Systems Slides by Niloy Mukherjee;'\
            'Alternative Class - Online Processing Systems with Sanjay Aggarwal;'\
            'Alternative Class 2 - Online Processing Systems with Niloy Mukherjee;'\
            'Alternative Class 1 - Online Processing Systems with Niloy Mukherjee'

sec_list = 'Alternative Class - Online Processing Systems with Omkar Deshpande;'\
            'Alternative Class - Online Processing Systems Slides by Omkar Deshpande;'\
            'Alternative Class - Online Processing Systems Slides by Sanjay Aggarwal;'\
            'Alternative Class 2 - Online Processing Systems Slides by Niloy Mukherjee;'\
            'Alternative Class 1 - Online Processing Systems Slides by Niloy Mukherjee;'\
            'Alternative Class - Online Processing Systems with Sanjay Aggarwal;'\
            'Alternative Class 2 - Online Processing Systems with Niloy Mukherjee;'\
            'Alternative Class 1 - Online Processing Systems with Niloy Mukherjee'

checker(prim_list, sec_list)
