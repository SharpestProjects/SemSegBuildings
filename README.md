
# Technical Take-Homes

After you have read this document, please provide us with your feedback **[here](https://forms.gle/YuGLJdDTN4meMFDU8)**. Thank you!

## Preliminary Notes

- 1. Read **all** assignment descriptions before you start with any, even the ones that don't necessarily match your specific job interests. Be open minded & deliberate with the ones you choose! Make an outline of which ones you want to do, and how you plan on attacking them before you start any solutions. Future you will be very grateful!

- 2. This repository assumes a working knowledge of Git/GitHub. If you have any issues you can consult the web or our mentors/mentees.

- 3. For the open ended assignments, use any programming language/technology you think best matches the description. Try to use as little dependencies as possible and make sure your code is clean and concise. If an assignment provides starter code and is a language you are not familiar with and are not willing to learn for whatever reason, please reach out so we can discuss.

- 4. Completing all assignments is not necessary, ideally you want to put in as much thought into your solutions as possible. Employers value quality > quantity especially when hiring a data scientist/machine learning engineer who's analyses/forecasts could directly contribute to the successes/failures of their products.

## Submissions

- Create a fork of this repository. Your fork will be private, however those added to this repository will be able to view it. Try not to look at other's forks: be authentic to yourself! -- your interpretation is unique and is what you will be evaluated on in a real world scenario. If you're having an issue or would like some input, bring it up in a discussion, the conversation will be much more helpful than simply reading other mentee's code alone.

- Organize your fork. -- Make sure each submission is self-contained in its own sub-directory so it's easier to review.

- Commit often. Since this isn't a "real world project", your commits don't have to be so much as formal descriptions of code modification, but in this environment try to describe your thought process. Your fork will act as a journal to see how your solution evolved and what you were thinking. Some popular challenge tools like [HackerRank](https://www.hackerrank.com/) will provide your evaluator with a detailed history of the code evolution. That means deletions, additions, long pauses, page leaves (assumed external resource usage) etc. So having a 3-dimensional view of your thought process will allow you to see your mistakes, triumphs, aha-moments, and overall progress. This also provides your mentors with the tools to give more in-depth feedback.

- When you believe you have done an assignment to the best of your abilities, let us know! Make sure to send an email to `dyllanmccreary@gmail.com` with your fork link & which assignment you are submitting. Ideally provide us with some parts you struggled with, were proud of, and any questions/comments you'd like for us to address. 

## Assignment Routes

There are 2 assignment "routes" currently available as well as one independent assignment. You may skip prerequisites, more detailed instructions will be found in each individual description section of applicable assignments.

If you choose to skip prerequisites for route #1, you will have to find a substitute dataset. to complete assignments #2/3 OR work with a partner who is willing to provide their dataset for you.

For route #2, you may skip #4 all together, however the dataset you will be working with will be sub-optimally structured.

### Recommended Usage:

![Flow chart visualization](https://i.gyazo.com/96e3c8c1f3dad3f6d8248ebe956dddb9.png)

## Assignment Outlines

### 1. _Custom Data Generation_

#### Description:

- This assignment, as well as it's follow ups (assignments #2 & #3), are purposefully left ambiguously open ended. There is no starter code for this assignment as we want to see how you structure a project right off the bat. Some companies will use challenge tools like [HackerRank](https://www.hackerrank.com/) which are diverse in structuring. Sometimes the format will be like this assignment - no starter code/data sets, others will provide a data set but no starter code, and occasionally you will have both starter code & data sets to work with. This is very situational, use this assignment as an opportunity to mold your interpretation to what your personal career aspirations are.

#### Spec:

- 1. Choose a file format/representation of any kind. Be creative! Some cool examples are: MP3, GIF, CAD, DWG. Make sure it interests you and aligns with positions you're applying for for maximum impact. File types aren't the only applicable data, this could also be sequences, simple matrices, etc.

- 2. The data you generate should have the following properties:
	
	- **Organized into sets.** -- You should have a Train and Test set with variable sizes for model repeatability. This will make it easier to do the follow up assignment. No validation set is necessary since your evaluator (a reviewing party) will be able to generate a new Test set and run it against new data.
	
	- **Categorical by nature.** -- This data should have a purpose, meaning the generated set should be separable into categories, whatever those may be. For example, using PNG as our file type, if our categories are [Green, Yellow, Blue], then "Yellow" data should be generated such that it is discernible in comparison. IE. containing a large amount of yellow pixels relative to other non-"Yellow" data.
		
		- **OPTIONALLY** this data could be non-categorical. IE. if the hypothetical application you come up with requires a model such as sequence to sequence. This is more advanced but also requires a bright and creative mind! However, this will require further modification to the assignment description. Please consult with a mentor if you would like to choose this route.
	
	- **Labeled.** -- According to the nature of your data (categorical or not) make sure you have a label associated with each data point.
	
	- **Clean, but not too clean.** -- This data should contain noise. Further using the PNG example, we don't want all of our "Yellow" data to be only yellow pixels - and only using variations within a threshold would be boring! Get creative on how to generate discrepancies. If this data is being ran through a model for training, we want it to be able to separate signal from noise. For this example, maybe you want some green and blue pixels in our "Yellow" data, but still have yellow pixels dominate.
	
	- **Spatially minimal.** -- Big data is huge in data science/machine learning, and the last thing we want is for our data set to be larger than necessary. If you have 1,000,000,000 training samples that are 1% redundant in the way they're stored, that is 10,000,000 more samples we could be storing in the same amount of space. So get creative with how you are storing your data. Yes, this is somewhat limited to the file type you are choosing, but if you're using, say RGB images, find a way to compress them such that signal is preserved. **BE CREATIVE!!**

- 3. Give your data a back story! What is this data's real life purpose? This doesn't have to be perfectly thought out, but it's helpful to gauge a good solution when you have a clear cut problem to solve.

- 4. Write a data generation script in the language you think best fits the problem or whatever you're most familiar with.

- 5. Save to an output directory in a format appropriate for the data you are supplying. As mentioned previously, make sure you have separated your data into train & test sets.

---

### 2. _Visualizations for Custom Generated Data_

*NOTE:  If you do not to wish to take part in the data generation assignment, despite being highly encouraged to if you are pursuing this line of assignments, you may also use a preexisting data set. Make sure to cite the source of your data.*

#### Description:

- This assignment is a direct follow up to assignment #1. In order to do this one you need to have either submitted your own version of #1, or gotten with a partner to either trade or build upon their submission. You are encouraged to consider another mentee's submission, doing your own is definitely great and will serve to be sufficient practice, however it will be interesting for everyone to bring a bit of collaboration into the mix. This serves as an opportunity to further provide/receive input on each other's data generators, as well as work with a data set that you don't have an intimate relationship with. If you do choose to build on top of another person's submission, please provide a link to the data generator's GitHub fork within your script file as a comment and let the mentors know when you get started/within your submission email.

- Given a data set, create a number of visualizations that help communicate the nature of the data in a way that is comprehensible to non-technically-centric business/executive roles.

#### Spec:

- 1. Do/use a partner’s assignment #1. If using someone else’s, make sure at the beginning of your file you include a link to their fork and note that the data generator is not contained within your own repository.

- 2. Put together a script that generates 2-3 visualizations of the data set. You can use any visualization library you choose, but try to keep the dependencies to a minimum. Again, quality > quantity so don't focus on getting a lot of visualizations, but rather spend the time to come up with great ones.

- 3. Your visualizations should have the following properties:

	- **Digestible.** -- You don't want to overwhelm people with a super complex visualization model. Keep it simple yet impactful.

	- **Meaningful.** -- It's up to you to decide what features you are wanting to present. If the data you are visualizing is diabetes prediction information, a meaningful visualization is one that shows which data points correlate to a prediction as well as ones that don't.

	- **Interesting.** -- Spend some time making your visualizations appealing! Though function is more important than form, that doesn't mean you should neglect it. There's a reason companies hire UX Engineers, and it's not because they need the extra tax write off, it's because retention is very important especially (as a use case example) during an executive briefing.

- 4. If your visualizations are static, ideally submit your work by providing those static outputs in your email. 

---

### 3. _Model for Custom Generated Data_

*NOTE:  If you do not to wish to take part in the data generation assignment, despite being highly encouraged to if you are pursuing this line of assignments, you may also use a preexisting data set. Make sure to cite the source of your data.*

#### Description:

- This assignment is also a direct follow up to assignment #1. The same collaboration process found in assignment "_Visualizations for Custom Generated Data (Data Science)_" applies here as well.

- Given a data set, develop a machine learning model that maps input data points to their expected outputs.

#### Spec:

- 1. Do/use a partner's assignment #1. If using someone else's, make sure at the beginning of your file you include a link to their fork and note that the data generator is not contained within your own repository.

- 2. Build a model that is applicable to the data set you are working with. Don't just settle with the first one that comes to mind, play around for a bit and really get intimate with the problem.

- 3. In your model script, provide a brief summary of what model you used, why you used it, and some possible alternatives with reasons why you went with the model you built over them. This write up will serve as an outline for when you are asked to articulate your intuition. This is very important in the interview process, a hiring manager wants to see what your critical breakdown would look like in a real world scenario.

---

### 4. _Data Migration/Reformatting_

#### Description:

- You are given 5 CSV files containing data relevant to an eCommerce store. This data was collected by a former engineer at this eCommerce company in a very... niche manner, to say the least. Your job is to come up with a new data format and clean up the existing data to match it. They also forgot to label a users gender in a meaningful way. Leave this as 0 & 1 for now. -- More on this in the following assignment "_Business Data Analysis_".

#### Spec:

- 1. Your input data is found in this repository in the `data_migration` sub-directory.

- 2. Take a look at the data, get an idea of what is in there and what it represents and think about what is necessary to keep. Assume this data was generated today.

- 3. Brain storm a few ways you may want to restructure this data. Come up with 2-3 different ways and note their pros and cons. Your output structure should in some way encompass the following features:
	- **Each item's/listing's pricing and their categories.** -- We want to know what items are available for purchase and what meta data they have. 
	- **User metadata.** -- There is meta data contained within these CSVs and we want to preserve as much as possible. What date did these users last login on? Remember, this data was generated today!
	- **User's purchases.** -- We want to know what users have purchased what items.

- 4. Write a script that takes in these 5 CSVs and transfers them into your selected optimal structure. Make sure to include these output CSVs in your fork. **NOTE:** You do not need exactly 5 output CSVs. It could be 1, or even 10 -- this is up to you!

---

### 5. _Business Data Analysis_

*NOTE:  If you do not to wish to take part in the data migration/reformatting assignment, despite being highly encouraged to if you are pursuing this line of assignments, you may instead use the raw CSV files used as input to the data migration/reformatting assignment (though it will be a pain to work with).*

#### Description:

- This assignment is a direct follow up to assignment #4. In order to do this one you need to have either submitted your own version of #4, or gotten with a partner to either trade or build upon their submission. You are encouraged to consider another mentee's submission, doing your own is definitely great and will serve to be sufficient practice, however it will be interesting for everyone to bring a bit of collaboration into the mix. This serves as an opportunity to further provide/receive input on each other's data reformation, as well as work with a data set structure that you don't have an intimate relationship with. If you do choose to build on top of another person's submission, please provide a link to the data reformatter's GitHub fork within your script file as a comment and let the mentors know when you get started/within your submission email.

- You are tasked to analyze the newly reformatted eCommerce data in order to help their marketing team personalize ads and recommendations better for their users to increase sales and decrease account inactivations.

#### Spec:

- 1. Do/use a partner's assignment #4. If using someone else's, make sure at the beginning of your file you include a link to their fork and note that the data reformatter is not contained within your own repository.

- 2. There are a number of features the marketing team needs access to in order to create a sale increasing strategy. Gather the following data points:
	- **Gender.** -- As stated in assignment #5, we have a number representing which user is which gender, however we do not know if they correspond to male or female. In your submission, you must provide which numerical value represents which gender group **and** the percentage of your certainty. You are given 2 hints:
		- Males are **less** likely to purchase from the Children & Electronics categories.
		- Females are **less** likely to purchase from the Books & Furniture categories.
	- **Category Popularity.** -- How popular is each category overall?
	- **Age Spending.** -- How much does each age group spend relative to each other? Also, which age groups should we more aggressively market to, and why? Age groups:
		- (-∞, 18), [18, 25), [25, 40), [40, ∞)
	- **Deactivated Accounts.** -- This one's more open ended: Are there any ways we can predict if an account will deactivate? Account deactivations are deliberately done by the user. If we can predict this, how? Also, how can the marketing team go about making it less likely for users to deactivate their accounts?
	- **Other Analyses.** - There are other hidden priors/anomalies in the data that will be useful for the marketing team. See if you can find any others not listed above! -- This is closer to real life where you aren't handed a bunch of features they want to see correlation to, but rather you as a Data Scientist will have to be sharp enough to sniff out. Even the smallest deviance could be useful. Don't be stubborn with your findings!

- 3. After you have collected the necessary data as detailed in the previous step, put together a report with your findings. Structure your report formally, treat it as though you were going to submit this to the executives at your future position. Do **not** put this report in your repository, simply attach it to your submission email.

---

### 6. _Video-Frame Speed Inference_

#### Description:

- This assignment is externally hosted. It was picked for it's simplicity and literal applicability as it is an actual company's Machine Learning Engineer code challenge ([comma.ai](https://comma.ai/)). You may choose to do it yourself for your own practice as well as use it to apply directly to CommaAI! You do not have to submit your solution to us, if you don't wish to, however we can still give you feedback before/after you send it to them, should you choose to.

#### Spec:

- Click [here](https://github.com/commaai/speedchallenge) to view.

---

After you have read this document, please provide us with your feedback **[here](https://forms.gle/YuGLJdDTN4meMFDU8)**. Thank you!

