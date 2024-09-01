import './JobInfo.css';
import { useEffect, useState } from 'react';
import jobService from '../../../services/jobService';
import companyService from '../../../services/companyService';
import MiniStatisticCard from '../MiniStatistic/MiniStatistic';
import JobTable from '../../JobTable/JobTable';


function JobInfo() {

  const [toggle,setToggle] = useState<boolean>(false)

  const [jobDetails, setJobDetails] = useState({
    viewedJobs: '',
    notViewedJobs: '',
    starJobs: '',
    count: ''
  });

  useEffect(() => {
    const getJobDetails = async () => {
      try {
        const details = await jobService.getJobsDetails();
        const companies = await companyService.getCompanies();
        const companiesCount = companies.count;

        setJobDetails({
          viewedJobs: details.viewed,
          notViewedJobs: details.not_viewed,
          starJobs: companiesCount,
          count: details.count
        });
      } catch (error) {
        console.error('Failed to fetch job details:', error);
      }
    };
    
    getJobDetails();
  }, [toggle]);

  return (
    <>
      <div className='task-employee-info'>
        <MiniStatisticCard title='Viewed Jobs' value={jobDetails.viewedJobs} />
        <MiniStatisticCard title='Not Viewed Jobs' value={jobDetails.notViewedJobs} />
        <MiniStatisticCard title='Companies' value={jobDetails.starJobs} />
        <MiniStatisticCard title='Jobs' value={jobDetails.count} />
      </div>
      <JobTable toggle={toggle} setToggle={setToggle}/>
    </>
  );
}

export default JobInfo;
