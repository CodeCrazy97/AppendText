# AppendText
This Python script will open up a journal file (a simple txt file) so the user can jot down the highlights from the previous week and/or from two weeks ago. 

The program calculates the dates of the Sundays for the previous week and for two weeks earlier. For example, suppose I ran the program on July 16, 2019. The date of the Sunday for the previous week would be "July 7, 2019". (So, this date will only be correct if the program is ran during the week after the events. If I am recording events for the week of July 7 - July 13, 2019, the date part of the program would be correct only if the program is ran during the week of July 14 - July 20, 2019.) The Python script would check if there is a journal entry for July 7, 2019. It would also check for a journal entry from two weeks earlier (June 30, 2019). One of three things could be true about these dates being in the script file:

	-	The July 7, 2019 entry is missing. In this case, the script will add "*** Week of July 7, 2019 ***" to the journal file and open it for the user to write about things that happened that week. 
	-	The June 30, 2019 entry is missing. In this case, the script will add "*** Week of June 30, 2019 ***" to the journal file and open it for the user to write about things that happened that week. 
	-	Both dates are missing. In this case, the file will add both lines of text to the file and open the file so the user can record events for both weeks.
