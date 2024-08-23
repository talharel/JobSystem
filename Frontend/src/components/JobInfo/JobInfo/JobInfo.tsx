import './JobInfo.css';
import MiniStatisticCard from '../MiniStatistic/MiniStatistic';

function JobInfo() {
  return (
    <>
      <div className='task-employee-info'>
        <MiniStatisticCard title='Viewed Jobs' value={'abcd'} />
        <MiniStatisticCard title='Not Viewed Jobs' value={'abcd'} />
        <MiniStatisticCard title='Star Jobs' value={'abcd'} />
        <MiniStatisticCard title='Total Jobs' value={'abcd'} />
      </div>
    </>
  );
}

export default JobInfo;
