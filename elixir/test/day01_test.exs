defmodule Day01Test do
  use ExUnit.Case

  test "calculate example 1" do
    input = "+1, +1, +1"
    assert Day01.calculate(input) == 3
  end

  test "calculate example 2" do
    input = "+1, +1, -2"
    assert Day01.calculate(input) == 0
  end

  test "calculate example 3" do
    input = "-1, -2, -3"
    assert Day01.calculate(input) == -6
  end

  test "find reached twice example 1" do
    input = "+1, -1"
    assert Day01.find_reached_twice(input) == 0
  end

  test "find reached twice example 2" do
    input = "+3, +3, +4, -2, -4"
    assert Day01.find_reached_twice(input) == 10
  end

  test "find reached twice example 3" do
    input = "-6, +3, +8, +5, -6"
    assert Day01.find_reached_twice(input) == 5
  end

  test "find reached twice example 4" do
    input = "+7, +7, -2, -7, -4"
    assert Day01.find_reached_twice(input) == 14
  end
end
