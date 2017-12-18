class Hamming
  def self.compute(dna_a, dna_b)
    raise ArgumentError if dna_a.length != dna_b.length

    dna_a.chars.map.with_index do |char, index|
      if char != dna_b[index]
        1
      else
        0
      end
    end.reduce(:+) || 0
  end
end
