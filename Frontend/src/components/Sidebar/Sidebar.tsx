import { Drawer, List, ListItem, ListItemIcon, ListItemText, Divider } from '@mui/material';
import WorkOutlineIcon from '@mui/icons-material/WorkOutline';
import PersonAddAlt1Icon from '@mui/icons-material/PersonAddAlt1';

function Sidebar(){
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 240,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 240,
          boxSizing: 'border-box',
        },
      }}
    >
      <List>
        <ListItem button>
          <ListItemIcon><WorkOutlineIcon  /></ListItemIcon>
          <ListItemText primary="Add Job" />
        </ListItem>
        <ListItem button>
          <ListItemIcon><PersonAddAlt1Icon /></ListItemIcon>
          <ListItemText primary="Add Recruiter" />
        </ListItem>
      </List>
      <Divider />
    </Drawer>
  );
};

export default Sidebar;
