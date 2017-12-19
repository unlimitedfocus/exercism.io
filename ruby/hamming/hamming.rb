class Hamming
  def self.compute(dna_a, dna_b)
    raise ArgumentError if dna_a.length != dna_b.length

    index = 0
    dna_a.chars.count do |x| 
      result = (x != dna_b[index])
      index += 1
      result
    end
  end
end
