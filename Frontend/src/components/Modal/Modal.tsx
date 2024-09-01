import Box from '@mui/material/Box';
import './Modal.css'
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';

const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

interface ModalProps {
  open: boolean;
  setOpen: (isOpen: boolean) => void;
  children: React.ReactNode;
}
export default function BasicModal({ open, setOpen, children }: ModalProps) {
  
  return (
    <div>
      <Modal
        open={open}
        onClose={()=>setOpen(false)}
      >
        <Box className='modal-box' sx={style}>
          {children}
        <Button fullWidth className='modal-closeButton' onClick={()=>setOpen(false)}>Close</Button>
        </Box>

      </Modal>
    </div>
  );
}
