import math

# Colors
black_color = '\033[0;30m'
red_color = '\033[0;31m'
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
blue_color = '\033[0;34m'
purple_color = '\033[0;35m'
cyan_color = '\033[0;36m'
gray_color = '\033[1;30m'
end_color = '\033[0m'

print()

can_names = ['#1 Picnic',  '#1 Tall', '#2', '#2.5', '#3 Cylinder',
             '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]


def main():

    best_cost_efficiency = 0
    best_storage_efficiency = 0

    for i in range(len(can_names)):
        volume = compute_volume(can_radius[i], can_height[i])

        cost_efficiency = compute_cost_efficiency(volume, can_cost[i])
        if cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency

        storage_efficiency = compute_storage_efficiency(can_radius[i], can_height[i])
        if storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency

        print(f'{red_color}¬{end_color} Can name: {can_names[i]}')
        print(f'\t{green_color}-{end_color} Storage efficiency: {green_color}{storage_efficiency:.2f}{end_color}')
        print(f'\t{green_color}-{end_color} Cost efficiency: {green_color}{cost_efficiency:.2f}{end_color}\n')

    print(f'{red_color}[!]{end_color} Best storage efficiency: {green_color}{best_cost_efficiency:.2f}{end_color}')
    print(f'{red_color}[!]{end_color} Best cost efficiency: {green_color}{best_storage_efficiency:.2f}{end_color}\n')


def compute_volume(radius, height):
    return math.pi * math.pow(radius, 2) * height


def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)


def compute_storage_efficiency(height, radius):
    return compute_volume(height, radius) / compute_surface_area(height, radius)


def compute_cost_efficiency(volume, cost):
    return volume / cost


main()
