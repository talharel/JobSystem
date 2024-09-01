import { useEffect, useState } from 'react';
import './JobTable.css';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import jobService from '../../services/jobService';
import Typography from '@mui/material/Typography';
import { TypeJob } from '../../utils/types';

interface JobTableProps {
  toggle: boolean;
  setToggle: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function JobTable({ toggle, setToggle }: JobTableProps) {
  const [jobs, setJobs] = useState<TypeJob[]>([]);

  useEffect(() => {
    const getJobs = async () => {
      try {
        const data = await jobService.getJobs();
        setJobs(data);
      } catch (error) {
        console.error('Failed to fetch jobs:', error);
      }
    };

    getJobs();
  }, [toggle]);

  async function handleRowClick(job: TypeJob) {
    await jobService.updateStatus(job.id, 'viewed');
    setToggle(!toggle);
    window.open(job.url, '_blank');
  }

  async function handleSearchJobs() {
    try {
      await jobService.searchJobs();
    } catch (error) {
      console.error('Failed to fetch job details:', error);
    }
  }

  return (
    <>
      <Typography variant='h6' component='h2' gutterBottom>
        Platform jobs
      </Typography>
      <TableContainer component={Paper} sx={{ maxHeight: 260 }}>
        <Table stickyHeader aria-label='jobs table'>
          <TableHead>
            <TableRow>
              <TableCell style={{fontSize:18}} className='job-cell' align='left'>
                Company
              </TableCell>
              <TableCell style={{fontSize:18}} className='job-cell' align='left'>
                Url
              </TableCell>
              <TableCell align='right'>
                <button
                  className='platform-modalButton'
                  onClick={handleSearchJobs}
                >
                  Find Jobs
                </button>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {jobs.map((job, index) => (
              <TableRow
                key={index}
                style={
                  job.status === 'viewed'
                    ? { background: 'rgba(27, 199, 54, 0.4)' }
                    : { background: 'white' }
                }
                onClick={() => handleRowClick(job)}
                sx={{ cursor: 'pointer' }}
              >
                <TableCell align='left'>{job.company_name}</TableCell>
                <TableCell align='left'>
                  <a href={job.url} target='_blank' rel='noopener noreferrer'>
                    {job.url}
                  </a>
                </TableCell>
                <TableCell></TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}
