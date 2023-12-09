
defmodule Main do
  import Enum
  def get_digits(s) do
    Regex.scan(~r/\d+/, s) |> map(&(&1 |> at(0)))
  end

  def calc_dist(dist, rec) do
    dist = String.to_integer(dist)
    rec = String.to_integer(rec)

    0..dist |> map(&((dist - &1 )* &1)) |> filter(&(&1 > rec)) |> length()
  end

  def silver do

    input = File.read!("input.txt") |> String.split("\n")
    times = get_digits(input |> at(0))
    distances = get_digits(input |> at(1))

    ans = zip(times,distances) |> map(&(calc_dist(elem(&1,0),elem(&1,1)))) |> IO.inspect() |> reduce(1,&(&1 * &2))
    IO.puts("Silver: #{ans}")


  end

  def gold do
    input = File.read!("input.txt") |> String.split("\n")
    time = input |> at(0) |> String.replace(~r/[^\d]/,"")
    distance = input |> at(1) |> String.replace(~r/[^\d]/,"")
    ans = calc_dist(time, distance)
    IO.puts("Gold: #{ans}")
  end
end
Main.silver()
Main.gold()
