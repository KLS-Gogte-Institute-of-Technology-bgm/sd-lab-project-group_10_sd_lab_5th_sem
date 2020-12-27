[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=286712&assignment_repo_type=GroupAssignmentRepo)

### Parking Management System

Four types of user :<br/>
1.admin<br/>
2.MANAGER<br/>
3.WATCHMAN<br/>
4.Customer(user)<br/>

Admin : Admin has an access to all the database. He/she will be the superuser.<br/>
Manager : Will be having the functionality of ManageVehicle,Ticket,VehicleCategory,Analysis,SearchVehicle,SLot,Timeup. <br/>
Watchman : Will have a responsiblity to create Ticket and have functionality to manageVehicle,analysis,SearchVehicle,Timeup.<br/>
Customer(user): Customer can Register the information and can login he/she will be given a functionality of dashboard,bookTicket and profile.Here a user can book an Ticket through online mode and and also update there profile.<br/>

# Parking Management System
Parking management system provides a portal to book slot for parking . Even user can manage there profile and also book parking slot throught online mode,They can also see the dashboard to view number of slot which are free and manager can maintain the account. This portal provides the analysis report where it shows the today parking statics and till now parking statics and also provides the search functionality.

## Tool used to build
**Client side**
1. HTML
3. Javascript
4. CSS

**Server side**
1. Django

**Database** - Sqllite

**Project by -** <br>
1.Prajwal  	    2GI18CS092   	   7338014988<br>
2.Rahul    	    2GI18CS105  	   6362957312<br>
3.Rakesh  	    2GI18CS106  	   9449499734<br>
4.Rohan   	    2GI18CS110  	   9148807891 <br>

# Youtube link for this project
[Youtube link Clink here](https://www.youtube.com/watch?v=wtBXErDHQNk)<br>


# Wiki page link<br>
[Manage Wiki link](https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/wiki/Manager)<br>
[Customer Wiki link](https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/wiki/Customer)<br>
<br>

# Local setup for this project
<p>To clone this repository and run the following commands :</p>
<pre><code>git clone https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem.git<br/></code></pre>
<p>Go to sd-lab-project-group_10_sd_lab_5th_sem/parking</p>
<pre><code>cd sd-lab-project-group_10_sd_lab_5th_sem/parking<br/></code></pre>
<p>Activate python environment :</p>
<pre><code>source parking-env/bin/active<br/></code></pre>
<h3>1. Migrate the model using following commands : </h3>
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
<p>Create super user :</p>
<pre><code>python manage.py createsuperuser</code></pre>
<p>create super user name,email,password,confirm password then run following commands:</p>
<img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/1.jpeg"  width="600" height="350">
<br/>
<pre><code>python manage.py runserver</code></pre>
<h3>2. go to url "127.0.0.1/admin" and login, Then create group in Groups</h3>
<img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/4.jpeg"  width="600" height="350">
<h3>2. Create three group admin,manager,customer,watchman </h3>
<img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/5.jpeg"  width="600" height="350">
<br/>
<h3>3. Create credentials for Manager</h3>
<p>create it in Users</p>
<img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/7.jpeg"  width="600" height="350">
 <h3>and check the  checkbox of superuser,staff status and chosen groups as manager</h3>
 <img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/8.jpeg"  width="600" height="350">
 <br/>
 <h3>4. Create credentials for Watchman. create it in Users </h3>
<img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/9.jpeg"  width="600" height="350">
 <h3>and check checkbox active,staff status and chosen groups as watchman</h3>
 <img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/10.jpeg"  width="600" height="350">
 <br/>
 <h3>5. chosen groups as admin</h3>
 <img src="https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/blob/master/images/11.jpeg"  width="600" height="350">
 <br/>
 <p>Logout from admin pannel</p>
 <h3>6 .Now be in the folder where manage.py is present and run command as</h3>
<pre><code>python manage.py runserver</code></pre>
<p>By default it will be login as superuser. Just logout on top right and try to login as manager username and password which you created during superuser login</p>
<p> Copy and paste the url in browser or type "127.0.0.1:8000" in browser</p>

# Wiki page link<br>
[Manage Wiki link](https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/wiki/Manager)<br>
[Customer Wiki link](https://github.com/KLS-Gogte-Institute-of-Technology-bgm/sd-lab-project-group_10_sd_lab_5th_sem/wiki/Customer)<br>
<br>
