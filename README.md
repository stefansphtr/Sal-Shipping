# <img src="./src/img/GIF%20Codecademy.gif" width="50"> Sal's Shipping <img src="./src/img/GIF%20Codecademy.gif" width="50">


<p align="center">
  <a href="#">
    <img src="https://badges.pufler.dev/visits/stefansphtr/Sal-Shipping" alt="Visits Badge">
    <img src="https://badges.pufler.dev/updated/stefansphtr/Sal-Shipping" alt="Updated Badge">
    <img src="https://badges.pufler.dev/created/stefansphtr/Sal-Shipping" alt="Created Badge">
    <img src="https://img.shields.io/github/contributors/stefansphtr/Sal-Shipping" alt="Contributors Badge">
    <img src="https://img.shields.io/github/last-commit/stefansphtr/Sal-Shipping" alt="Last Commit Badge">
    <img src="https://img.shields.io/github/commit-activity/m/stefansphtr/Sal-Shipping" alt="Commit Activity Badge">
    <img src="https://img.shields.io/github/repo-size/stefansphtr/Sal-Shipping" alt="Repo Size Badge">
  </a>
</p>

## 📝 Description

Sal's Shipping is a Python program that helps users determine the most cost-effective shipping method for their packages. Given the weight of a package, the program calculates the cost of shipping via ground shipping, drone shipping, or premium ground shipping, and then recommends the cheapest method.

## 📚 Table of Contents

- [ Sal's Shipping ](#-sals-shipping-)
  - [📝 Description](#-description)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔧 Requirements](#-requirements)
  - [💡 How it Works](#-how-it-works)
  - [🚀 Usage](#-usage)
  - [Example](#example)
  - [📖 Useful Resources](#-useful-resources)
  - [🧪 Tests](#-tests)

## 🔧 Requirements

To run this project, you will need:

- Python 3.x

## 💡 How it Works 

The program uses three main functions, each defined in the [`shipping.py`](src/shipping.py) file:

- `calculate_ground_shipping_cost(weight)`: Calculates the cost of ground shipping based on the package's weight.
- `calculate_drone_shipping_cost(weight)`: Calculates the cost of drone shipping based on the package's weight.
- `find_cheapest_shipping_method(weight)`: Determines the cheapest shipping method for a given weight.

The user is prompted to enter the weight of their package, and the program then prints the cheapest shipping method and its cost. The user can continue to calculate shipping for other packages or exit the program.

This program is part of Sal's Shippers, a service dedicated to providing users with the most cost-effective shipping solutions. Whether you're a small business looking to save on shipping costs or an individual sending a gift to a loved one, Sal's Shipping is here to ensure you get the best shipping rates possible.

## 🚀 Usage

To use this application, simply run the `shipping.py` script in your Python environment:

```bash
python src/shipping.py
```
The script will prompt you to enter the weight of your package. Enter the weight as a float (for example, `4.5` for a 4.5 pound package).

The script will then print the cheapest shipping method and its cost.

The script will ask if you want to calculate shipping for another package. Enter `yes` to calculate shipping for another package, or `no` to exit the script.

## Example

Here's an example of what you might see when you run the script:

```bash
$ python src/shipping.py
Please enter the weight of the package: 18.5
The cheapest method is Ground Shipping and it will cost $ 107.88
Do you want to calculate shipping for another package? (yes/no): no
```
In this example, the user entered a package weight of `18.5` pounds. The script then printed the cheapest shipping method and its cost. The user then chose to exit the script.

## 📖 Useful Resources

- [Python Documentation](https://docs.python.org/3/)
- [Python Input](https://www.w3schools.com/python/ref_func_input.asp)
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Python Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Python Conditionals](https://www.w3schools.com/python/python_conditions.asp)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp)
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)

## 🧪 Tests

Currently, there are no tests for this application. Contributions to add tests are welcome.

---

This README is always kept up-to-date with the latest changes to the project. It is written in English for global accessibility. If you have any suggestions to improve this README, please feel free to contribute.