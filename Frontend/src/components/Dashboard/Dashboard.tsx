import { Grid } from '@mui/material';
import './Dashboard.css';
import Sidebar from '../Sidebar/Sidebar';
import JobInfo from '../JobInfo/JobInfo/JobInfo'
import FavoriteTable from '../FavoriteTable/FavoriteTable';

const Dashboard = () => {
  return (
    <Grid container spacing={2}>
      <Grid item xs={2}>
        <Sidebar />
      </Grid>
      <Grid item xs={10}>
        <div className='dashboard-content'>
          <JobInfo />
          <FavoriteTable />
        </div>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
