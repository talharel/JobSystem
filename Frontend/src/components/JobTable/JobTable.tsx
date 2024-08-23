import { useEffect, useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import jobService from '../../services/jobService';
import { TypeJob } from '../../utils/types';

export default function JobTable() {
  const [jobs, setJobs] = useState<TypeJob[]>([]);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const data = await jobService.getTasks();
        console.log(data);
        setJobs(data);
      } catch (error) {
        console.error('Failed to fetch jobs:', error);
      }
    };

    fetchJobs();
  }, []);

  const handleRowClick = (url: string) => {
    window.open(url, '_blank');
  };

  return (
    <TableContainer component={Paper} sx={{ maxHeight: 400 }}>
      <Table stickyHeader aria-label="jobs table">
        <TableHead>
          <TableRow>
            <TableCell align="left">Company</TableCell>
            <TableCell align="left">Url</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {jobs.map((job) => (
            <TableRow
              key={job.id}
              onClick={() => handleRowClick(job.url)}
              sx={{ cursor: 'pointer' }}
            >
              <TableCell align="left">{job.company_name}</TableCell>
              <TableCell align="left">
                <a href={job.url} target="_blank" rel="noopener noreferrer">
                  {job.url}
                </a>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
