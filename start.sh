while getopts "d" arg
do 
	case $arg in
		d)
			# stop all containers
		        docker-compose -f deployment.yml down
			exit 0
			;;
	        \?)
			echo "unknow args $args with value $OPTARG" 
	                exit 1
			;;
	esac
done
if [ -f hostip.secret ]; then
    rm hostip.secret
fi
hostip=`hostname -I | cut -d ' ' -f1` 
echo "HOST_IP=$hostip" > hostip.secret
docker-compose -f deployment.yml up --build -d
