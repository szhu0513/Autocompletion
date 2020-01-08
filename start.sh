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
docker-compose -f deployment.yml up --build -d
