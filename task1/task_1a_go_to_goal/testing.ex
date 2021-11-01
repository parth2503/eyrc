defmodule Test do
  def add(a,b) do
    a+b

  end

  def add3(a,b,c) do
    IO.puts add(add(a,b),c)*

  end
end
