import dataSumamry as ds
import eda
import inferences as inf
#ds.dataSummaryMod("h9gi-nx95")
data=eda.exploratoryDataAnalysis()
inf.inferences(data)
print("Conclusion:")
print("""So from the above EDA and the analysis I found that there is a seasonality in the variation of no of rashes across the months like first 3 quaters of the calendar year with large number of crashes and last quater being with less number of crashes so Traffic or Transport department should be more vigilent in those days and public as well need to take an extra mile interms of safety and also Driver Inattention/ Distraction is the main reason for the crashes so people has to keep this in mind while driving. And Interestingly I found that more crashes has beemn happeneing during the weekdays Tuesday and Thursday and in the timing from 2pm to 7pm this might be due to week day work ending and office closure hours.And also Brokloyn, Queens and manhattan has the highest number of crashes across the streets Broadway, Atlantic and 3rd avenue being the most.
From this findings repsective authority of the governament can take preventive measures to acoid the crashes by deploying more traffic police force at the above mentioned areas at particular times across the all risky and dangerous areas.""")





