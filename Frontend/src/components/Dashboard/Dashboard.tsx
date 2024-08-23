import { Grid } from '@mui/material';
import './Dashboard.css';
import Sidebar from '../Sidebar/Sidebar';
import JobInfo from '../JobInfo/JobInfo/JobInfo'
import JobTable from '../JobTable/JobTable'

const Dashboard = () => {
  return (
    <Grid container spacing={2}>
      <Grid item xs={2}>
        <Sidebar />
      </Grid>
      <Grid item xs={10}>
        <div className='dashboard-content'>
          <JobInfo />
          <JobTable />
        </div>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
