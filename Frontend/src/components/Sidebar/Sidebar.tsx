import {
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider,
  Box,
  TextField,
  Button,
} from '@mui/material';
import WorkOutlineIcon from '@mui/icons-material/WorkOutline';
import companyService from '../../services/companyService';
import GradeIcon from '@mui/icons-material/Grade';
import computer from '../../assets/computer.jpeg'
import BasicModal from '../Modal/Modal';
import { useState } from 'react';


function Sidebar() {

  const [openModal, setOpenModal] = useState<boolean>(false);
  const [companyName, setCompanyName] = useState<string>('');
  const [companyUrl, setCompanyUrl] = useState<string>('');

  async function handleAddCompany() {
    companyService.addCompany(companyName,companyUrl)
    setOpenModal(false)
  }



  return (
    <Drawer
      variant='permanent'
      sx={{
        width: 240,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 240,
          boxSizing: 'border-box',
        },
      }}
    >
        <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          margin:'20px'
        }}
      >
        <img 
          src={computer} 
          alt="Your Image" 
          style={{ width: '80%', maxWidth: 150 }}
        />
        
      </Box>
      <Divider />
      <List>

        <ListItem button>
          <ListItemIcon>
            <WorkOutlineIcon />
          </ListItemIcon>
          <ListItemText primary='Add Job' />
        </ListItem>


        <ListItem button>
          <ListItemIcon>
          <GradeIcon />
          </ListItemIcon>
          <ListItemText onClick={()=>setOpenModal(true)} primary='Add Company' />
        </ListItem>
      <Divider />
      </List>
    <BasicModal open={openModal} setOpen={setOpenModal} children={
              <BasicModal
              open={openModal}
              setOpen={setOpenModal}
              children={
                <div>
                  <TextField
                    label='Enter Company'
                    variant='outlined'
                    fullWidth
                    margin='normal'
                    onChange={(e)=>setCompanyName(e.target.value)}
                  />
                  <TextField
                    label='Enter Url'
                    variant='outlined'
                    fullWidth
                    margin='normal'
                    onChange={(e) => setCompanyUrl(e.target.value)}
                  />
                  <Button
                    onClick={() => {
                      handleAddCompany()
                      setOpenModal(false);
                    }}
                    variant='contained'
                    fullWidth
                  >
                    Send
                  </Button>
                </div>
              }
            />
    } />
    </Drawer>
  );
}

export default Sidebar;
