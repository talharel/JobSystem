import { Card, CardContent, Typography, Box } from '@mui/material';
import StarIcon from '@mui/icons-material/Star';
import DoneIcon from '@mui/icons-material/Done';
import PriorityHighIcon from '@mui/icons-material/PriorityHigh';
import WorkOutlineIcon from '@mui/icons-material/WorkOutline';
const MiniStatistic = ({ title, value }:{title:string,value:string}) => {
  let iconComponent;
  let iconColor;

  switch (title) {
    case 'Viewed Jobs':
      iconComponent = <DoneIcon fontSize='large' />;
      iconColor = '#4caf50';
      break;
    case 'Not Viewed Jobs':
      iconComponent = <PriorityHighIcon fontSize='large' />;
      iconColor = '#d742f5';
      break;
    case 'Companies':
      iconComponent = <StarIcon fontSize='large' />;
      iconColor = '#42d4f5';
      break;
    case 'Jobs':
      iconComponent = <WorkOutlineIcon fontSize='large' />;
      iconColor = '#83deca';
      break;
    default:
      iconComponent = null;
  }

  return (
    <Card sx={{ width:340,height:60,display: 'flex', alignItems: 'center', padding: 2, boxShadow: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', width: 60, height: 60, backgroundColor: iconColor, borderRadius: '50%' }}>
        {iconComponent}
      </Box>
      <CardContent sx={{ flex: 1 }}>
        <Typography variant="h6" component="div">
          {title}
        </Typography>
        <Typography variant="h4" color="text.secondary">
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default MiniStatistic;
