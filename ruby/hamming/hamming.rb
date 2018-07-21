class Hamming
  def self.compute(dna_a, dna_b)
    raise ArgumentError if dna_a.length != dna_b.length
    (0..dna_a.length).count {|i| dna_a[i] != dna_b[i] }
  end
end
