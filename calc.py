def calculate_louvres(glass_drop, divider_height_on_glass, min_pitch=28, max_pitch=56, step=0.1, max_divider_adjustment=25):
    # Calculate the total length of the stile by adding the glass drop and 46 mm (additional length for stile)
    total_stile_length = glass_drop + 46
    # Define the size of the top and bottom rails
    top_bottom_rail_size = 50
    # Calculate the initial height of the divider including additional 25 mm
    divider_height_with_rails = divider_height_on_glass + 25

    # Initialize the best configuration as None
    best_configuration = None

    # Loop through possible divider adjustments within the range
    for divider_adjustment in range(-max_divider_adjustment, max_divider_adjustment + 1):
        # Calculate the adjusted position of the divider
        divider_position = divider_height_with_rails + divider_adjustment

        # Calculate the available space below and above the divider
        bottom_space = divider_position - top_bottom_rail_size
        top_space = total_stile_length - divider_position - top_bottom_rail_size

        # Initialize bottom pitch to the maximum pitch
        for bottom_pitch in [x * step for x in range(int(max_pitch / step), int(min_pitch / step) - 1, -1)]:
            # Calculate the number of louvres that fit in the bottom space
            bottom_louvres = int(bottom_space / bottom_pitch)
            if bottom_louvres == 0:
                continue
            # Calculate the gap left after fitting the louvres
            bottom_gap = bottom_space - bottom_louvres * bottom_pitch

            for top_pitch in [x * step for x in range(int(max_pitch / step), int(min_pitch / step) - 1, -1)]:
                # Calculate the number of louvres that fit in the top space
                top_louvres = int(top_space / top_pitch)
                if top_louvres == 0:
                    continue
                # Calculate the gap left after fitting the louvres
                top_gap = top_space - top_louvres * top_pitch

                # Ensure the number of louvres is a whole number for both top and bottom
                if bottom_louvres == int(bottom_louvres) and top_louvres == int(top_louvres):
                    # Calculate the total gap for the current configuration
                    total_gap = bottom_gap + top_gap
                    # Update the best configuration if the current one has fewer louvres or smaller total gap
                    if (best_configuration is None or
                            bottom_louvres + top_louvres < best_configuration[1] + best_configuration[3] or
                            (bottom_louvres + top_louvres == best_configuration[1] + best_configuration[3] and total_gap < best_configuration[5])):
                        best_configuration = (bottom_pitch, bottom_louvres, top_pitch, top_louvres, divider_position, total_gap)

    # Return the best configuration if found
    if best_configuration:
        return best_configuration[0], best_configuration[1], best_configuration[2], best_configuration[3], best_configuration[4]

    # Return None if no valid configuration is found
    return None, None, None, None, None

# Example values
glass_drop = int(input("What is the glass drop? "))
divider_height_on_glass = int(input("What is the divider height? "))  # Input the divider height on the glass drop

# Calculate the best configuration for the louvres
bottom_pitch, bottom_louvres, top_pitch, top_louvres, divider_position = calculate_louvres(glass_drop, divider_height_on_glass)

# Print the results
print(f"Bottom Pitch: {bottom_pitch} mm")
print(f"Bottom Louvres: {bottom_louvres}")
print(f"Top Pitch: {top_pitch} mm")
print(f"Top Louvres: {top_louvres}")
print(f"Divider Position: {divider_position} mm")
