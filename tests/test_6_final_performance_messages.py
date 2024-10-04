max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
import re

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_6_final_performance_messages(test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(test_cases, list):
            raise ValueError("test_cases should be a list of dictionaries. Contact your professor.")

        combined_normalized_printed = ''
        final_1, final_2, final_3 = ["qualified for the ncaa soccer tournament", "you had a good season", "your team needs to practice"]
        flag_1, flag_2, flag_3 = [False, False, False]
        found_phrases = []
        # Loop through each test case
        for test_case in test_cases:
            try:
                # Grab the necessary data from the test case dictionary
                inputs = test_case["inputs"]
                num_repeat_iterations = 50

                # repeat test case 30 times, should have a 99.9999% chance of finding a tie score if it exists.
                for _ in range(num_repeat_iterations):
                    # Load in the student's code and capture output
                    _, captured_output, _ = load_student_code(inputs, test_case)

                    # Split the captured output into lines
                    captured_lines = captured_output.splitlines()
                    
                    # Normalize the captured output to remove spaces, punctuation, and symbols
                    normalized_captured_print_statements = [normalize_text(captured_print) for captured_print in captured_lines]
                    normalized_captured_print_statements = '\n'.join(normalized_captured_print_statements)
                    combined_normalized_printed += f"\n{normalized_captured_print_statements}"

                    if (final_1 not in normalized_captured_print_statements
                        and final_2 not in normalized_captured_print_statements
                        and final_3 not in normalized_captured_print_statements):
                        assert False, format_error_message(
                    custom_message=(f"Your code should always print out one of these 3 options, but currently does not:\n\n "
                                    f"{final_1, final_2, final_3}\n\n"
                                    f"Double check your spelling, or that your if statement logic makes a final season message always print.\n\n"
                                    f"Below are all the printed messages from your code (ignoring punctuation / capitalization):\n\n"
                                    f"{combined_normalized_printed}\n\n"),
                    test_case=test_case,
                    display_inputs=True,
                )

                    # checking if each final message appears at least once
                    # simultaneously checks that the other statements don't appear to 
                    # incorrectly pass code that just prints the statements each time.
                    if (final_1 in normalized_captured_print_statements
                        and final_2 not in normalized_captured_print_statements
                        and final_3 not in normalized_captured_print_statements):
                        flag_1 = True
                        found_phrases.append(final_1)

                    elif (final_2 in normalized_captured_print_statements
                        and final_1 not in normalized_captured_print_statements
                        and final_3 not in normalized_captured_print_statements):
                        flag_2 = True
                        found_phrases.append(final_2)

                    elif (final_3 in normalized_captured_print_statements
                        and final_2 not in normalized_captured_print_statements
                        and final_1 not in normalized_captured_print_statements):
                        flag_3 = True
                        found_phrases.append(final_3)

                    if flag_1 and flag_2 and flag_3:
                        break
                        
                assert flag_1 and flag_2 and flag_3, format_error_message(
                    custom_message=(f"Your code should print out at least one of these final season messages after each season:\n\n "
                                    f"{final_1, final_2, final_3}\n\n"
                                    f"But, across 50 repeats of your code, only these get printed:\n\n"
                                    f"{found_phrases}\n\n"
                                    f"Double check your spelling, or that your if statement logic makes a final season message always print.\n\n"
                                    f"Below are all the printed messages from your code (ignoring punctuation / capitalization):\n\n"
                                    f"{combined_normalized_printed}\n\n"),
                    test_case=test_case,
                    display_inputs=True,
                )

            except AssertionError:
                raise
            
            except Exception as e:
                # Handle other exceptions
                exception_message_for_students(e, test_case)
    
    # the first AssertionError raises the problem here, this raises it to the main level so the test will stop
    except AssertionError:
        raise

    except Exception as outer_e:
        # Catches any problem in grabbing the test cases
        test_case = {"id_test_case": None}
        exception_message_for_students(outer_e, test_case=test_case) 