def scoring(array)  
    array.each do |user|
        # call update_score on `a` here
        # update_score of every user in the array unless the user is admin
        unless user.is_admin?
            user.update_score
        end   
    end
end