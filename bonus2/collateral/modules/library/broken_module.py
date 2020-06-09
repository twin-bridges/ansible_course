#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = dict(
        name=dict(type="str", required=True),
        new=dict(type="bool", required=False, default=False),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    result = dict(changed=True, original_message="Something", message="It worked!!!")

    # Syntax error--my_var doesn't exist at this point
    # try:
    #    print(my_var)
    # except NameError as e:
    #    module.fail_json(msg=str(e))

    output = "Something went wrong. "
    output += "I am gathering all this information from my program"
    result["output"] = output
    module.exit_json(**result)


if __name__ == "__main__":
    main()
