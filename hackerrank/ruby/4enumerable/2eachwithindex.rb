def skip_animals(animals, skip)
  # Your code here
    result_array = []
    
    animals.each_with_index do |item, index|
        result_array.push("#{index}:#{item}") if index >= skip
    end
    result_array    
end