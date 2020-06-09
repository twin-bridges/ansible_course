#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():

    # Define your modules arguments
    module_args = dict(
        name=dict(type="str", required=True),
        new=dict(type="bool", required=False, default=False),
    )

    # Create an instance of the AnsibleModule class
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Define standard results
    result = dict(changed=False, original_message="Something", message="It worked!!!")

    # Return items as JSON
    module.exit_json(**result)


if __name__ == "__main__":
    main()
