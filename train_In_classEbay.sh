nohup python train_mx_ebay_margin.py --gpus=0 --batch-k=2 --batch-size=80 --use_pretrained --use_viz --name=Ebay_Inclass --data=EbayInClass >mytrainEbay_Inclass.log 2>&1 &