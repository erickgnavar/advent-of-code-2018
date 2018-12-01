defmodule Day01 do
  defp convert_input_to_numbers(input) when is_binary(input) do
    input
    |> String.split(",")
    |> Enum.map(&String.trim/1)
    |> Enum.filter(fn x -> String.length(x) > 0 end)
    |> Enum.map(&String.to_integer/1)
  end

  def calculate(input) when is_binary(input) do
    input
    |> convert_input_to_numbers()
    |> Enum.reduce(fn x, acc -> x + acc end)
  end

  def find_reached_twice(input) when is_binary(input) do
    input
    |> convert_input_to_numbers()
    |> _find_reached_twice()
  end

  defp _find_reached_twice(values, frequency \\ 0, counter \\ %{}, found \\ false) do
    if found do
      frequency
    else
      [head | tail] = values

      if Map.has_key?(counter, frequency) do
        _find_reached_twice(tail ++ [head], frequency, counter, true)
      else
        _find_reached_twice(
          tail ++ [head],
          frequency + head,
          Map.put(counter, frequency, 1),
          false
        )
      end
    end
  end

  def run() do
    raw =
      File.read!("../inputs/day01.txt")
      |> String.replace("\n", ",")

    result =
      raw
      |> calculate()

    reached_twice =
      raw
      |> find_reached_twice()

    IO.puts("The reached frecuency is #{result}")
    IO.puts("The first frequency reached twice is #{reached_twice}")
  end
end
