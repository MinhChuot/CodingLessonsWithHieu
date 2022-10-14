# fischer random rules:
	# there can be only 2 knights, 2 bishops, 2 rooks, 1 queen and 1 King and 8 pawns
	# the white pawns must start at 2nd rank
	# the black pawns must start at 7th rank
	# the pieces must start at the back ranks (ranks 1 and 8)
	# bishops must be on opposite-colored-squares
		# i.e. bishops can't stand on squares such that there is a space of 1,3,5 or 7 squares between those squares
		# i.e. the number of squares that fill the gaps between the squares with bishops can only be 0,2,4 or 6

# chess960 rules:
	# same as fischer random, except that:
	# there has to be a rook on either side of the king, 
		# i.e. both rooks cannot be on the same side of the king, 
		# i.e. kings cannot be in the corners

