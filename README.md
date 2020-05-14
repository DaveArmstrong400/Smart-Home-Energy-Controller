# Smart-Home-Energy-Controller
Major Individual Design Project as part of MEng Integrated Design Engineering Degree at the University of Bath.

The code contained in the repository allows for;
1. An image to be taken using a Raspberry Pi model 3B board and camera module
2. The image to be sent to an online server for archiving via a 'Post' request and corresponding PostHDrive.PHP script
3. Image processing script to extract the meter reading and save it to a csv file, before posting to the server
4. Powershell script to stream the meter reading and related calculations to a live gauge on the user interface which was created using Microsoft's Power Bi program

The aim of this project was to reduce domestic consumption by an average of 25% per household (~3900kWh), with the market wide aim of leading the U.K to their net zero emissions by 2050 target. But how can this be achieved in the current market where smart meters are provided free of charge from utility providers?

Four key areas were outlined to give power to the consumer whilst actively engaging them to use the device for their own benefit;
1. Actionable energy saving measures; tested for effort vs savings for guaranteed results
2. Automated meter reading; retrofittable meter imaging device that can be installed without technical expertise with no invasive measures as to cause damage to the utility provider's equipment
3. Education; easy to understand reports highlighting areas of high consumption compared to cost and individual environmental impact
4. Long-term habit changes overcoming the four-week novelty of smart meters; competition, accountability and consumer benefits
